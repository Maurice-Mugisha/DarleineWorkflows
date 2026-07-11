<?php


if(isset($_GET['specific_role'])):


	$role_id = isset($_GET['role_id']) ? $fieldValidator->validate_field($_GET['role_id']) : "";

	$roleprivilegemap_array = array();
	$privilege_array = array();
	$role_array = array();

	$query = $queryExecutor->execute($selectionObj->select_role($role_id));

	while($row = mysqli_fetch_array($query)):

		$role_id = $row['role_id'];
		$role_array[$role_id] = array();
		$role_array[$role_id]['role_id'] = $role_id;

		$key = $role_id;

		$dependent_query = $queryExecutor->execute($selectionObj->select_role_name($role_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$role_array[$key]['name'] = $row_col['name'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_role_description($role_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$role_array[$key]['description'] = $row_col['description'];


		$secondary_query = $queryExecutor->execute($selectionObj->select_roleprivilegemap_by_role($role_id));

		while($sec_row = mysqli_fetch_array($secondary_query)):

			$privilege_id = $sec_row['privilege_id'];
			$privilege_array[$privilege_id] = array();
			$privilege_array[$privilege_id]['privilege_id'] = $privilege_id;

			$sec_key = $privilege_id;

			$dependent_query = $queryExecutor->execute($selectionObj->select_privilege_name($privilege_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$privilege_array[$sec_key]['name'] = $row_col['name'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_privilege_description($privilege_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$privilege_array[$sec_key]['description'] = $row_col['description'];

		endwhile;



	endwhile;


?>

<table cellspacing = "1" cellpadding = "0" align = "center" width = "100%" id = "roleprivilegemap">
 <tr>
 <td colspan = "3">&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td colspan = "2"><a href="target_print.php?roleprivilegemap&&role_id=<?= $role_id ?>" target="_blank" style="color:#00FF00;">Print PDF</a></td></tr>
 <tr class = "top_row">
 <td>&nbsp;&nbsp;#&nbsp;&nbsp;</td>
 <td>&nbsp;Privilege id&nbsp;</td>
 <td>&nbsp;Name&nbsp;</td>
 <td>&nbsp;Description&nbsp;</td>
 <td>&nbsp;&nbsp;Actions&nbsp;&nbsp;</td></tr>
 
<?php $i = 0; ?>


<?php  foreach($privilege_array as $privilege_key => $privilege_value): ?>
<?php $css_class = ($i+1)%2 == 0 ? "even_row" : "odd_row"; ?>


<tr>
	<td><?= ($i+1) ?></td>
	<td><?= $privilege_value['privilege_id'] ?></td>
	<td><?= $privilege_value['name'] ?></td>
	<td><?= $privilege_value['description'] ?></td>
	<td>

		<?php $id_string = $privilege_id; ?>

		<div id="update_privilege_<?= $id_string ?>" style="display:none" class="updates">
		<table border="0" align="center" class="overlay_contained_table">
		<tr>
			<td align="right">
			<div class="closebtn" id="close_circle" onclick="closeUpdateOverlay('update_privilege_<?= $id_string ?>');">&nbsp;&times;&nbsp;</div>
			</td>
		</tr>
		<tr><td><br /></td></tr>
		<tr>
			<td align="center">
			<fieldset style="width: 80%">
			<legend>privilege Information</legend>
			<?php update_privilege($queryExecutor, $selectionObj, $updateObj, $fieldValidator, $privilege_value['privilege_id']); ?>
			</fieldset>
			</td>
		</tr>
		<tr>
			<td><br /></td>
		</tr>
		</table>
		</div>


<?php

	$roleprivilegemap_count = count_roleprivilegemap($queryExecutor, $selectionObj);
	$mapping_link = "roleprivilegemap.php?privilege&&privilege_id=".$privilege_value['privilege_id']."";
	$title = "roleprivilegemap corresponding entries.";
	$label = "Rol.";
	get_mapping_mark_up($roleprivilegemap_count, $mapping_link, $title, $label);



?>


	<label id="update_link_<?= $id_string ?>" onclick="showUpdate('update_<?= $id_string ?>');" style="cursor:pointer">
	<img src="images/icons/edit.png" width="15px" height="15px" title="edit entry" style="cursor:pointer" />
	</label> 
 &nbsp; 
	<?php 
		$link = "privilege.php?delete_Privilege&&privilege_id=".$privilege_value['privilege_id']."";
		$message = "";
	?>

	<?php showConfirmDeleteAction($id_string, $link, $message); ?>
	<label style="cursor:pointer" onclick="showDelete('delete_<?= $id_string ?>')">
	<img src="images/icons/delete.png" width="15px" height="15px" title="delete entry" />
	</label>
	</td>
<tr>
	<?php $i = ($i + 1); ?>
<?php endforeach; ?>
 <tr>
 <td colspan = "5"></td></tr></table>

<?php endif; ?>



<?php

function get_mapping_mark_up($entity_count, $mapping_link, $title, $label){

	if($entity_count > 0):

?>
		<a href="<?= $mapping_link ?>" target="_blank" title="<?= $title ?>" style="color: #000033; font-weight:bold;">
			<font size="-1"><?= $label ?></font>
		</a>
		&nbsp;
<?php
	endif;
}

?>